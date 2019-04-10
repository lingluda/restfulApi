package main

import (
	"database/sql"
	"fmt"
	_"github.com/go-sql-driver/mysql"
)
func main(){
// db,err:=sql.Open("mysql","root:root@tcp(localhost:3306)/lld?charset=utf8");
     if err != nil {
        fmt.Println(err);
    }
	 //查询数据，取所有字段
    rows2, _ := db.Query("select * from sys_table");
    //返回所有列
    cols, _ := rows2.Columns();
    // fmt.Println(cols);
    //这里表示一行所有列的值，用[]byte表示
    vals := make([][]byte, len(cols));
    //fmt.Println(vals);
    //这里表示一行填充数据
    scans := make([]interface{}, len(cols));
    //这里scans引用vals，把数据填充到[]byte里
    for k, _ := range vals {
        scans[k] = &vals[k];
    }
    //fmt.Println(scans);
    i := 0;
    result := make(map[int]map[string]string);
    for rows2.Next() {
        //填充数据
        rows2.Scan(scans...);
        //每行数据
        row := make(map[string]string);
        //把vals中的数据复制到row中
        for k, v := range vals {
            key := cols[k];
            //这里把[]byte数据转成string
            fmt.Println(string(v))
            row[key] = string(v);
        }
        //放入结果集
        result[i] = row;
        i++;
    }
    fmt.Println(result);
    //关闭数据库，db会被多个goroutine共享，可以不调用
    defer db.Close();
	}