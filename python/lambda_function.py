import json
import psutil
import socket

def lambda_handler(event, context):

    return {
        'statusCode': 200,
        'hostname': socket.gethostname(),
        'processor': psutil.cpu_percent(interval=1),
        'memory': psutil.virtual_memory().percent,
        'swap': psutil.swap_memory().percent,
        'disk': psutil.disk_usage('/').percent,
        'ip': socket.gethostbyname(socket.getfqdn())
    }

