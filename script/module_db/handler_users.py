import sqlite3
from connect import *



@ConnectBase
def Test(value: str, cursor: sqlite3.Cursor):
    sql = f"SELECT id FROM users WHERE FIO = ?"
    cursor.execute(sql, (value, ))
    result = cursor.fetchall()
    print(result)


# Test("Иванов Иван Иванович")


# edit
@ConnectBase
def CreateNewUser(value, cursor) -> bool | None:
    """
    Данная метод добовляет нового пользователя в базу данных
    :return: возращает True если операция прошла успешно при любых других действий возращает None
    """
    sql = "SELECT id FROM users WHERE FIO = ?"
    cursor.execute(sql, (value, ))
    result = cursor.fetchall()
    print(result)


@ConnectBase
def SearchUser(fio: str = None, student_id_number: int = None, number_group: int = None, cursor = sqlite3.Cursor) -> tuple[tuple, ...] | tuple:
    """
    Данный метод осуществляет поиск пользователей по введенной информации
    :param fio: ФИО пользователь
    :param student_id_number: номер студенческого билета 
    :param number_group: номер группы
    :param cursor: курсор для базы данных вводится автоматический
    :return: возращает найденную информацию в tuple(tuple, ...) если информация не найдена возращает пустой tuple() 
    None - при ошибки подключение к базе данных и False при отсуствие вводных данных
    """

    sql = "SELECT id FROM users WHERE "

    info = {}

    # Мейби удалить, но пока останеться здесь
    if not any(fio, student_id_number, number_group):
        return False
        # raise ValueError 

    if fio is not None:
        info["FIO = ?"] = fio


    if student_id_number is not None:
        info["student_id_number = ?"] = student_id_number


    if number_group is not None:
        info["number_group = ?"] = number_group

    sql += " AND ".join(tuple(info.keys())) + ';'
        

    cursor.execute(sql, tuple(info.values()))
    result = cursor.fetchall()
    return result

        # if len(result) == 1:
        #     print("one")
        #     return result[0]

        # elif len(result) >= 2:
        #     print("several")
        #     return False        
        # else:
        #     print("zero")
        #     return None




    # @ConnectBase
    # def AddNewUser():
    #     sql = f"SELECT id FROM users WHERE FIO = ?"
    #     cursor.execute(sql, (value, ))
    #     result = cursor.fetchall()

# Test("Иванов Иван Иванович")

def SearchIdStudent(fio: str, number_group: int = None, student_id_number: int = None):
    try:
        with sqlite3.connect(f"{WAY_TO_BASE}") as connect:
            cursor = connect.cursorsor()

            sql = "SELECT id FROM users WHERE FIO = ?"
            argument_array = [fio]


            if number_group is not None:
                sql += " AND number_group = ?"
                argument_array.append(number_group)
            
            if student_id_number is not None:
                sql += " AND student_id_number = ?"
                argument_array.append(student_id_number)

            cursor.close()

            print(sql)
            cursor.execute(sql, argument_array)

            result = cursor.fetchall()

            print(result)

            if len(result) == 1:
                print("one")
                return result[0]

            elif len(result) >= 2:
                print("several")
                return False        
            else:
                print("zero")
                return None
            
    except sqlite3.Error as error_base:
        print(error_base)
    except Exception as error:
        print(error)
    finally:
        cursor.close()





# def CreateNewUser(fio: str, number_group: int, phone_number: str = None, email: str = None, vk: str = None, telegram: str = None) -> bool | None:
def CreateNewUser() -> bool | None:
    """
    Данная функция добовляет нового пользователя в базу данных
    :return: возращает True если операция прошла успешно при любых других действий возращает None
    """
    try:
        with sqlite3.connect(f"{WAY_TO_BASE}") as connect:
            cursor = connect.cursorsor()
            # sql = f"INSERT INTO users('FIO', 'number_group', 'number_phone', 'email', 'vk', 'telegram') VALUES(?, ?, ?, ?, ?, ?);"
            # cursor.execute(sql, (fio, number_group, phone_number, email, vk, telegram))
            sql = f"SELECT id FROM users WHERE FIO = ?"
            # cursor.close()
            print(connect in locals())
            cursor.execute(sql, ("Иванов Иван Иванович", ))

            connect.commit()
            # print(cursor in locals())
            # cursor.close()
            print("da")
    except sqlite3.Error as error_base:
        print(error_base)
    except Exception as error:
        print(error)
    finally:
        cursor.close()
    connect.close()
    # cursor.close()

    print(connect in locals())
    # print(cursor in locals())






def AddTakeBook(user_id: int, book_id: int) -> bool | None:
    try:
        with sqlite3.connect(f"{WAY_TO_BASE}") as connect:
            cursor = connect.cursorsor()
            sql = f"INSERT INTO take_book('user_id', 'book_id', 'date_take') VALUES(?, ?, date('NOW'));"
            cursor.execute(sql, (user_id, book_id))
            connect.commit()
            cursor.close()
            return True
    except sqlite3.Error as error_base:
        print(error_base)
    except Exception as error:
        print(error)
    finally:
        cursor.close()



# edit