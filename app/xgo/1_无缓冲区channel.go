package main

import(
	"fmt"
	"time"
)
func main(){
	ch := make(chan int,0)
	fmt.Println("最初开始")
	go func(){
		for i:=0;i<3;i++{
			fmt.Println("子协程：i=%d",i)
			ch<-i
			fmt.Println("开始111")
		}
	}()
	time.Sleep(5*time.Second)
	for i:=0;i<3;i++{
		num:=<-ch
		fmt.Println(num)
	}
}