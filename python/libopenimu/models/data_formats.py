"""

"""
import sqlite3


class DataFormat:

    UINT8 = 0
    SINT8 = 1
    UINT16 = 2
    SINT16 = 3
    UINT32 = 4
    SINT32 = 5
    UINT64 = 6
    SINT64 = 7
    FLOAT32 = 8
    FLOAT64 = 9

    value_types = [UINT8, SINT8, UINT16, SINT16, UINT32, SINT32, UINT64, SINT64, FLOAT32, FLOAT64]
    value_names = ['UINT8', 'SINT8', 'UINT16', 'SINT16', 'UINT32', 'SINT32', 'UINT64', 'SINT64', 'FLOAT32', 'FLOAT64']

    @staticmethod
    def name(id_data_format):
        return DataFormat.value_names[id_data_format]

    @staticmethod
    def populate_database(conn):
        """ Will populate database with table tabDataFormat """
        try:
            for format_id in DataFormat.value_types:
                conn.execute("INSERT INTO tabDataFormat (id_data_format, name)"
                             "VALUES (?,?)", (format_id, DataFormat.value_names[format_id]))

        except Exception as e:
            print('Insert Error: ', str(e))

    @staticmethod
    def is_valid(id_data_format):
        return DataFormat.value_types.__contains__(id_data_format)