import sqlite3

db_name = 'lab_3.db'

#cur = db.cursor()
def main():
    while True:
        choice = get_choice()
        if choice == 'q':
            break
        if choice == '1':
            add_new()
        if choice == '2':
            show_all()

def records_db():
    with sqlite3.connect(db_name) as db:
        cur.execute('create table if not exists Chainsaw_Juggling_Record_Holders(juggler, country, catches)')

def add_new():
    juggler = input("Enter juggler's name: ")
    country = input('Enter country of origin: ')
    catches = int(input('Enter number of catches(as an integer): '))
    add_info_db(juggler, country, catches)

def add_info_db(juggler, country, catches):
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute('insert into Chainsaw_Juggling_Record_Holders values(?,?,?)', (juggler, country, catches))

def delete_record():
    with sqlite3.connect(db_name) as db:
        del_data = c.execute("DELETE FROM Chainsaw_Juggling_Record_Holder WHERE Name=?", (data3,))
        #cur.execute('delete from Chainsaw_Juggling_Record_Holders where id = ?')

def update_record():
    with sqlite3.connect(db_name) as db:
        update_info = c.execute



def get_choice():

    print('''
    Press 1 to add new record
    Press 2 to show all records
    Press 3 to delete record
    Press 4 to edit record
    Press q to quit program
    ''')
    return input('Enter choice: ')


if __name__ == '__main__':
    main()
