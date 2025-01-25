import logging
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from sqlalchemy.orm import Session
from app.db.models import ExampleModel

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SchedulerManager:
    """
    通用任务调度管理器
    用于管理定时任务和周期性任务
    """

    def __init__(self, max_threads=10):
        # 配置调度器的执行器
        executors = {
            'default': ThreadPoolExecutor(max_threads)
        }
        self.scheduler = BackgroundScheduler(executors=executors)

    def start(self):
        """启动调度器"""
        if not self.scheduler.running:
            self.scheduler.start()
            logger.info("调度器已启动")

    def stop(self):
        """停止调度器"""
        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)
            logger.info("调度器已停止")

    def add_cron_job(self, func, cron_rule, args=None, job_id=None, replace_existing=True):
        """
        添加 Cron 定时任务
        :param func: 任务函数
        :param cron_rule: cron 表达式，如 "0 9 * * *" 表示每天早上9点
        :param args: 任务函数的参数列表
        :param job_id: 任务ID
        :param replace_existing: 是否替换已存在的任务
        """
        trigger = CronTrigger.from_crontab(cron_rule)
        self._add_job(func, trigger, args, job_id, replace_existing)

    def add_interval_job(self, func, seconds=0, minutes=0, hours=0, args=None, job_id=None, replace_existing=True):
        """
        添加间隔任务
        :param func: 任务函数
        :param seconds: 间隔秒数
        :param minutes: 间隔分钟
        :param hours: 间隔小时
        :param args: 任务函数的参数列表
        :param job_id: 任务ID
        :param replace_existing: 是否替换已存在的任务
        """
        trigger = IntervalTrigger(
            seconds=seconds,
            minutes=minutes,
            hours=hours
        )
        self._add_job(func, trigger, args, job_id, replace_existing)

    def _add_job(self, func, trigger, args=None, job_id=None, replace_existing=True):
        """
        内部添加任务的通用方法
        """
        self.scheduler.add_job(
            func=func,
            trigger=trigger,
            args=args or [],
            id=job_id,
            replace_existing=replace_existing
        )
        logger.info(f"任务已添加: {job_id} (trigger: {trigger})")

    def remove_job(self, job_id):
        """
        删除任务
        :param job_id: 任务ID
        """
        try:
            self.scheduler.remove_job(job_id)
            logger.info(f"任务已删除: {job_id}")
        except Exception as e:
            logger.error(f"删除任务失败: {job_id}, 错误: {e}")

    def get_jobs(self):
        """获取所有任务"""
        return self.scheduler.get_jobs()

    def load_jobs_from_db(self, db_session: Session):
        """
        从数据库加载定时任务
        这里使用 ExampleModel 作为示例，实际使用时替换为你的模型
        """
        try:
            # 查询所有需要定时执行的任务
            tasks = db_session.query(ExampleModel).filter(
                ExampleModel.settings.contains({"scheduled": True})
            ).all()

            for task in tasks:
                # 从 settings 中获取调度配置
                schedule_config = task.settings.get("schedule", {})
                
                if schedule_config.get("type") == "cron":
                    self.add_cron_job(
                        func=self.execute_task,
                        cron_rule=schedule_config.get("cron"),
                        args=[task.id, task.name],
                        job_id=f"task_{task.id}"
                    )
                elif schedule_config.get("type") == "interval":
                    self.add_interval_job(
                        func=self.execute_task,
                        seconds=schedule_config.get("seconds", 0),
                        minutes=schedule_config.get("minutes", 0),
                        hours=schedule_config.get("hours", 0),
                        args=[task.id, task.name],
                        job_id=f"task_{task.id}"
                    )

            logger.info("已从数据库加载所有定时任务")
        except Exception as e:
            logger.error(f"加载定时任务失败: {e}")

    def pause(self):
        """暂停调度器"""
        if self.scheduler.running:
            self.scheduler.pause()
            logger.info("调度器已暂停")

    def resume(self):
        """恢复调度器"""
        if not self.scheduler.running:
            self.scheduler.resume()
            logger.info("调度器已恢复")

    @staticmethod
    def execute_task(task_id, task_name):
        """
        执行任务的示例方法
        :param task_id: 任务ID
        :param task_name: 任务名称
        """
        logger.info(f"执行任务: ID={task_id}, Name={task_name}")


