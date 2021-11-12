## TESTING TESTER

## IMPORT REQUIRED MODULES
import redis, time, requests
from rq import Queue

## DEFINE DEMO TASK
def background_task(n):
    ## DEFINE VARIABLES
    delay = 10
    counter = 1

    ## OUTPUT STATUS
    print("Task Running .....")
    print(f"Simulating {delay} second delay")

    ## FAKE A LONG RUNNING TASK
    #time.sleep(delay)
    while counter <= delay:
        ## ATTEMPT TO PUSH MESSAGE TO SOCKETIO
        ## TODO: MAKE THIS CONFIGURABLE
        requests.get('http://web:8080/api/v1/test', params={"msg": f"Delay: { counter }"})

        print (f"Delay: { counter }", flush=True)
        counter += 1
        time.sleep(1)

    ## OUTPUT STATUS
    print(len(n))
    print("Task Complete!")

    ## RETURN RESULTS
    return len(n)
