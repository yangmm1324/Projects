import sqlite3

## create memory database
def convertToBinaryData(filename):
    ## convert digital data to binary format
    with open(filename,'rb') as file:
        blobData=file.read()
    return blobData

def writeTofile(data,filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename,'wb') as file:
        file.write(data)


def readBlobData(photo,path):
    try:
        writeTofile(photo,path)
    except Exception as error:
        print('Failed to read blob data from sqlite table', error)


def create_schema():
    connection=sqlite3.connect('database.db')# open a connection to a database file named database.db
    with open('schema.sql') as f:
        connection.executescript(f.read())

def insertPost(user,title,content,visit_date, photo):
    try:
        connection=sqlite3.connect('database.db')# open a connection to a database file named database.db
        cursor=connection.cursor()
        print('conntected to sqlite3')
        if photo:
            photo=convertToBinaryData(photo)

        # convert data into tuple format
        data_tuple=(user,title,content,visit_date,photo)
        query=""" INSERT INTO posts
                                  (user,title, content, visit_date, photo) VALUES (?,?, ?, ?, ?)"""

        cursor.execute(query, data_tuple)
        connection.commit()
        print('Trip memory inserted successfully!')
        cursor.close()
    except sqlite3.Error as error:
        print('Failed to insert trip into sqlite table', error)
    finally:
        if (connection):
            connection.close()
            print('The sqlite connection is closed.')

def updatePost(title,content,visit_date, photo,id):
    try:
        connection=sqlite3.connect('database.db')# open a connection to a database file named database.db
        cursor=connection.cursor()
        if photo:
            photo=convertToBinaryData(photo)

        # convert data into tuple format
        data_tuple=(title,content,visit_date,photo)
        cursor.execute('UPDATE posts SET title=?, content=?, visit_date=?, photo=? WHERE id=?',
                                              (title,content,visit_date,photo,id))

        connection.commit()
        print('Trip memory updated successfully!')
        cursor.close()
    except sqlite3.Error as error:
        print('Failed to update the post!', error)
    finally:
        if (connection):
            connection.close()
            print('The sqlite connection is closed.')


def create_user():
    ####Create user database
    connect=sqlite3.connect('user.db')# open a connection to a database file named database.db
    with open('schema_user.sql') as f:
        connect.executescript(f.read()) # this section is to create the table defined in the schema

    cur=connect.cursor() # create a cursor object to execute the query

    cur.execute("INSERT INTO users(username,password,email) VALUES(?,?,?)", ("a1","p1",'yang@gmail.com'))
    print('User 1 inserted successfully')
    cur.execute("INSERT INTO users(username,password,email) VALUES(?,?,?)", ("a2","p2",'zhang@gmail.com'))
    print('User 2 inserted successfully')
    connect.commit()
    connect.close()

def main():

    insertPost('a1','Alaska','What a cool trip','12/18/2019','E:\Projects\BookStore\Alaska_Aurora.jpg')
    create_user()


if __name__=='__main__':
    main()
