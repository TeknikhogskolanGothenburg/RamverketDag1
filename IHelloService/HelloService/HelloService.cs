using System;

namespace HelloService
{
    public class HelloService : MarshalByRefObject, IHelloService.IHelloService
    {
        public string GetMessage(string name)
        {
            return "Hello " + name;
        }
    }
}
