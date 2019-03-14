def get_connection(db, user, host, password):
    from sqlalchemy import create_engine
    url = f'mysql+pymysql://{user}:{password}@{host}/{db}'
    return create_engine(url)

from env import user, host, pw

import pandas as pd

conn = get_connection('ada_students', user, host, pw)

qry = '''SELECT st.first_name, st.last_name,  gr.group_id, gr.student_id
FROM students as st
JOIN student_groups as gr
ON st.student_id = gr.student_id
WHERE gr.group_id = '7'
ORDER BY gr.group_id;'''

df_sql = pd.read_sql('select student_id, group_id from student_groups where module_id = 5;', conn)

df_sql2 = pd.read_sql(qry, conn)

print(df_sql2)