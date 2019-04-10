package main
 
import(
	"fmt"
	"net/http"
)
func say_hello(w http.ResponseWriter, req *http.Request){
	fmt.Fprint(w,"hello",req.PostFormValue)
}
func main(){
	http.HandleFunc("/",say_hello)
	http.ListenAndServe(":8888",nil)
}