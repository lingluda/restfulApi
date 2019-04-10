package main

import(
	"fmt"
	"time"
)
func main(){
	ch := make(chan int,3)
	fmt.Printf("缓冲区剩余数据个数：%d,缓冲区大小：%d",len(ch),cap(ch))
	go func(){
		for i:=0;i<20;i++{
			fmt.Printf("子协程[%d],len(ch):%d,cap(%d)\n",i,len(ch),cap(ch))
			ch<-i
		}
	}()
	time.Sleep(2*time.Second)
	for i:=0;i<20;i++{
		num:=<-ch
		fmt.Println(num)
	}
}