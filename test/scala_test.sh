#!/bin/sh
exec scala "$0" "$@"
!#
object HelloWorld {
  def main(args: Array[String]) {
    println("Hello, world! " + args.toList)
    var age:Int = 22
    println(age)
    age = 35
    println(age)
  }
}
HelloWorld.main(args)
