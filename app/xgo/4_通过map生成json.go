package main
import (
	"fmt"
	"encoding/json"
)
func main(){
	m:=make(map[string]interface{},4)
	m["company"]="fst"
	m["sub"]=[]string{"","java","python","c++","javascript"}
	m["isok"]=true
	m["price"]=8.99
	fmt.Println("map = ",m)
	
	//编码生产json
	result,err :=json.MarshalIndent(m,"","    ")
	if err!=nil{
		fmt.Println("err = ",err)
		return
	}
	fmt.Println("result = ",string(result))
}