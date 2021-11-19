import schedule
import time
import main
import datetime

now = datetime.datetime.now().strftime('%a')

match now:
    case 'Sat':
        schedule.every().saturday.at('7:35').do(main.main)
    case 'Sun':
        schedule.every().sunday.at('7:35').do(main.main)
    case 'Mon':
        schedule.every().monday.at('7:35').do(main.main)
    case 'Tue':
        schedule.every().tuesday.at('7:35').do(main.main)


while True:
    schedule.run_pending()
    time.sleep(10)