

int main()
{
    int a = 2;
    int b = 3;
    print(a, b);
    int* pa = &a;
    int* pb = &b;
    int t = *pb;
    *pb = *pa;
    *pa = t;
    print(a, b);
    return 0;
}