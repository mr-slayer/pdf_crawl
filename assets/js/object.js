function Student(name,age)
{
    this.name=name;
    this.age=age;
    this.fun=function()
    {
        document.write("<h2>this is "+this.name+" and having age:"+this.age+ "</h2>");
    }
    
}
var obj1= new Student("aakash",21);
var obj2=new Student("sagar",22);
obj2.fun();