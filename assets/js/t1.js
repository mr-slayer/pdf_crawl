var c=0;
for(var i=1;i<=20;i++)
{
    if(i%2==0)
    {
        document.write("<h2>" +i+"</h2>");
        c++;
    }
    
    
    if(c>=5)
    {
        break;
    }
    //document.write(x+"*"+i+"="+(x*i))
}