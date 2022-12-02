import requests
from pprint import pprint
get_task = 'https://b24-vgcuh0.bitrix24.com/rest/10/dhx2b3zg2lq30l1p/task.item.list.json'
get_emp = 'https://b24-vgcuh0.bitrix24.com/rest/10/dhx2b3zg2lq30l1p/lists.element.get.json?IBLOCK_TYPE_ID=bitrix_processes&IBLOCK_ID=46'

def task_info():
    r= requests.get(get_task).json()
    for task in r['result']:
        title = task['TITLE']
        description = task['DESCRIPTION']
        DEADLINE = task['DEADLINE']
        START_DATE_PLAN = task['START_DATE_PLAN']
        START_DATE_PLAN = task['START_DATE_PLAN']
        GROUP_ID = task['GROUP_ID']
        RESPONSIBLE_ID = task['RESPONSIBLE_ID']
        T_ID =task['ID']
        creeated_by = task['CREATED_BY']
        RESPONSIBLE_NAME = task['RESPONSIBLE_NAME']
        CREATED_BY_LAST_NAME = task['CREATED_BY_LAST_NAME']
        CREATED_DATE =task['CREATED_DATE']
        status = task['REAL_STATUS']
        CLOSED_BY=task['CLOSED_BY']

        print(status)


def emp_info():
    task_in_month2=[]
    f = open('taskid.txt','r')
    for i in f.readlines():
        task_in_month2.append(i)
    f.close()
    f= open('taskid.txt','a')

    c= 0 
    r = requests.get(get_emp).json()
    for emp in r['result']:
        emp_name=emp['NAME']
        #task_in_month
        for k ,l in emp['PROPERTY_600'].items():
            emp_task_in_month = l 
        #task in project
        for k ,l in emp['PROPERTY_602'].items():
            emp_project_in_month = l
        #print(emp_name,emp_project_in_month,emp_task_in_month) 
        r= requests.get(get_task).json()
        for task in r['result']:
            status = task['REAL_STATUS']
            RESPONSIBLE_NAME = task['RESPONSIBLE_NAME']
            T_ID =task['ID']
            title = task['TITLE']
            
            if emp_name in RESPONSIBLE_NAME :
                if status == '5':
                    for i in task_in_month2:
                        if T_ID  ==  i:
                            print('')
                        else:
                            print('new task completed' + emp_name , RESPONSIBLE_NAME,title)
                            f.writelines('\n'+T_ID)
                            


 
    f.close()        
        


emp_info()
