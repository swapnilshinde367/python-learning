# pylint: skip-file
# Mysql Connectivity using Python
import mysql.connector

objMysqlConnection	= mysql.connector.connect(	host		= 'localhost',
												database	= 'db_name',
												user		= 'root',
												password	= 'password' )



strQuery = 'INSERT INTO `test_table` \
(`user_name`, \
`original_tweet`, \
`translated_tweet`, \
`score`, \
`positive`, \
`negative`, \
`neutral`) \
VALUES \
(%s,%s,%s,%s,%s,%s,%s)'

objCursor = objMysqlConnection.cursor()
objCursor.executemany( strQuery, arrmixDataToInsert )
objMysqlConnection.commit()