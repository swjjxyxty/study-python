import logging

logging.basicConfig(level=logging.INFO)

logging.info("info msg...")
logging.debug("debug msg..")
logging.warning("warning msg...")
logging.error("error msg...")


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')
