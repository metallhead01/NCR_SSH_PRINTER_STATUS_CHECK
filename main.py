import paramiko
import time

#Начали выполнение
start_time = time.time()

host = '192.168.1.27'
user = 'root'
secret = 'admin'
port = 2222
answer = 0

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

print("Choice mode:\n\t1. 5 seconds\n\t2. 1 minute\n\t3. 30 minutes")

delay = None
while delay is None:
    choice = input()

    if choice == "1":
        delay = 5
    elif choice == "2":
        delay = 30
    elif choice == "3":
        delay = 1800
    else:
        print("Ты чо цифру от 1 до 3 ввести не можешь?!")

# Подключение
client.connect(hostname=host, username=user, password=secret, port=port)

while answer != -1:

    time.sleep(delay)

    # Выполнение команды
    stdin, stdout, stderr = client.exec_command('ifconfig')
    #stdin, stdout, stderr = client.exec_command('ping 192.168.137.111')

    # Читаем результат
    data = stdout.read() + stderr.read()

    answer = data.find(b'rndis0')
    print("Все ок.")

client.close()

print("Упал нахуй")
print("--- %s seconds ---" % (time.time() - start_time))
