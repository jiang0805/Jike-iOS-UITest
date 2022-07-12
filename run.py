
import time
import shutil
import json
import subprocess
from common.run_case import RunCases
from common.report import create_statistics_report, backup_report, zip_file_path
from common.base import Base
from common.log import Log
import os
from config import read_config


def run():
    cmd = ['tidevice', 'list', '--json']
    terminal_output = subprocess.check_output(cmd)
    devices = json.loads(terminal_output)[0]

    run_devices = RunCases(devices)
    log = Log()
    log.set_logger(run_devices.get_devices()['name'], os.path.join(run_devices.get_path(), 'client.log'))
    log.i('udid: %s' % run_devices.get_devices()['udid'])

    # 设置driver、设置报告路径, 必须在操作任何页面之前调用
    base_page = Base()
    base_page.set_path(run_devices.get_path())
    base_page.set_driver()
    base_page.start_app(read_config.ReadConfig().get_pkg_name())

    run_devices.run_cases()

    create_statistics_report(run_devices)
    start_time = time.strftime('%Y%m%d%H%M%S', time.localtime())
    backup_report('./TestReport', './TestReport_History', start_time)
    # zip_file_path('./TestReport_History/' + 'Report_' + start_time, './TestReport_History', start_time + ".zip")
    if os.path.exists(os.path.join(os.getcwd(), 'temp')):
        shutil.rmtree(os.path.join(os.getcwd(), 'temp'))


if __name__ == '__main__':
    run()
