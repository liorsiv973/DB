from __future__ import print_function
import psycopg2
import sys

def create_table(connection):
    trans = get_transaction(connection)
    table_str = "create table accounts(id integer primary key, owner varchar, balance integer);"
    insert_str = "insert into accounts values(1, 'alice', 100), (2, 'bob', 100), (3, 'claire', 100);"
    print("** Creating table:\n", table_str)
    trans.execute(table_str)
    print("** Inserting rows:\n", insert_str)
    trans.execute(insert_str)
    connection.commit()

def open_connection(username):
    return psycopg2.connect(database="public", user=username, host = "dbcourse")

def get_transaction(connection):
    return connection.cursor()

def apply_query(trans, i, query):
    trans.execute(query)
    rows = trans.fetchall()
    print("\nTRANSACTION",i)
    print("=============")
    print(query)
    for row in rows:
        print(row)

def close_connection(connection):
    connection.close()

def set_isolation_levels(trans1, trans2, level):
    print("** Setting isolation levels:\n", level)
    set_str = "set transaction isolation level " + level
    trans1.execute(set_str)
    trans2.execute(set_str)

def drop_table(con):
    trans = get_transaction(con)
    trans.execute("drop table accounts;")

def commit_transaction(con, i):
    print("\nTRANSACTION",i)
    print("=============")
    print("ATTEMPT COMMIT: ")
    con.commit()
    print("COMMIT SUCCEEDED")

def run_scenario_1(con1, con2, level):
    trans1 = get_transaction(con1)
    trans2 = get_transaction(con2)
    set_isolation_levels(trans1, trans2, level)
    apply_query(trans1, 1, "select * from accounts")
    apply_query(trans2, 2, "select * from accounts where id = 1")
    apply_query(trans1, 1, "update accounts set balance = balance - 10 where id = 1 returning *")
    apply_query(trans2, 2, "select * from accounts where id = 1")
    commit_transaction(con1, 1)
    apply_query(trans2, 2, "select * from accounts where id = 1")
    commit_transaction(con2, 2)

def run_scenario_2(con1, con2, level):
    trans1 = get_transaction(con1)
    trans2 = get_transaction(con2)
    set_isolation_levels(trans1, trans2, level)
    apply_query(trans1, 1, "select * from accounts")
    apply_query(trans2, 2, "select * from accounts where balance = 100")
    apply_query(trans1, 1, "insert into accounts values(4, 'dan', 100) returning *")
    apply_query(trans2, 2, "select * from accounts where balance = 100")
    commit_transaction(con1, 1)
    apply_query(trans2, 2, "select * from accounts where balance = 100")
    commit_transaction(con2, 2)

def run_scenario_3(con1, con2, level):
    try:
        trans1 = get_transaction(con1)
        trans2 = get_transaction(con2)
        set_isolation_levels(trans1, trans2, level)
        apply_query(trans1, 1, "select * from accounts")
        apply_query(trans1, 1, "insert into accounts select 5, 'trans1', sum(balance) from accounts returning *")
        apply_query(trans1, 1, "select * from accounts")
        apply_query(trans2, 2, "select * from accounts")
        apply_query(trans2, 2, "insert into accounts select 6, 'trans2', sum(balance) from accounts returning *")
        apply_query(trans2, 2, "select * from accounts")
        commit_transaction(con1, 1)
        commit_transaction(con2, 2)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    trans3 = get_transaction(con1)
    apply_query(trans3, 3, "select * from accounts")
    
if __name__ == '__main__':

    isolation_levels_dict = {"RC":"READ COMMITTED", "RR": "REPEATABLE READ", "S": "SERIALIZABLE"}
    scenario_dict = {"1": run_scenario_1, "2": run_scenario_2, "3": run_scenario_3}
    if len(sys.argv) != 4 or sys.argv[2] not in scenario_dict or sys.argv[3] not in isolation_levels_dict:
        print("Usage python run-scenarios.py <username> <schedule_num> <isolation_level>")
        print("Schedule number must be 1, 2 or 3. Isolation level must be RC, RR or S.")
        sys.exit(-1)

    try:
        con1 = open_connection(sys.argv[1])
        con2 = open_connection(sys.argv[1])
        create_table(con1)
        scenario_dict[sys.argv[2]](con1, con2, isolation_levels_dict[sys.argv[3]])
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con1 is not None:
            drop_table(con1)
            con1.commit()
            close_connection(con1)
            close_connection(con2)
