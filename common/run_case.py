import os
import pytest
import subprocess


class RunCases:
    def __init__(self, devices):
        self.devices = devices

        self.test_report_path = os.path.join(os.getcwd(), 'TestReport'
                                             + os.sep + self.devices['name'].replace(':', '_').replace(' ', '')
                                             + '_' + self.devices['udid'])

        if not os.path.exists(self.test_report_path):
            os.makedirs(self.test_report_path)

        self.tem_path = os.path.join(os.getcwd(), 'temp' + os.sep + devices["udid"])
        if not os.path.exists(self.tem_path):
            os.makedirs(self.tem_path)

        self.file_name = os.path.join(self.test_report_path, 'TestReport.html')

    def get_path(self):
        return self.test_report_path

    def get_devices(self):
        return self.devices

    def run_cases(self):
        temp_allure_path = self.tem_path
        html_report_path = self.test_report_path + '/html'
        # '-m', 'vic',
        args = ['-m', 'jw', '-W', 'ignore::DeprecationWarning', '-v', '-s', '--alluredir', temp_allure_path]
        pytest.main(args)

        # 生成html
        cmd = 'allure generate {} -o {} --clean'.format(temp_allure_path, html_report_path)
        subprocess.Popen(cmd, shell=True).communicate()


if __name__ == '__main__':
    print(os.path.join(os.getcwd(), 'TestReport'))
