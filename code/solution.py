# Lucas Amrhein - Assignment 3
def format_alert(severity, source_ip, alert_message):
   x='['+severity+']' +' - '
   y=source_ip +': '
   z=alert_message
   message=x+y+z
   return message