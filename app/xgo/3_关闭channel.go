package main
import(
	"fmt"
)
func main(){
	ch :=make(chan int)
	fmt.Println(len(ch),cap(ch))
	go func(){
		for i:=0;i<3;i++{
			ch<-i
		}
		close(ch)
	}()
	fmt.Println(len(ch))
	for num:=range ch{
		fmt.Println("num = ",num)
	}
	// for{
	// 	if num,ok:=<-ch;ok==true{
	// 		fmt.Println(num)
	// 	}else{
	// 		break
	// 	}
		
	// }
}