import click
import subprocess
import getpass

@click.command()
@click.option('--backup', '-b', is_flag=True, help='copy hosts file to new_file')
@click.option('--hosts_path', '-p', default='/etc/hosts', help='if /etc/hosts does not exist, please set hosts path')
@click.argument('new_file')
def replace(backup, hosts_path, new_hosts_file):
    # パスワードの入力
    passwd = (getpass.getpass() + '\n').encode()

    src = new_hosts_file
    dst = hosts_path

    if backup:
        dst, src = src, dst

    subprocess.run(('sudo', '-S', 'cp', src, dst), input=passwd, check=True)

if __name__ == '__main__':
    replace()
