int main() {
    int a[5];
    int i=0;
    int b;
    for (i; i < 5; i=i+1) {
        a[i] = i;
    }
    i = 0;
    for (i; i < 5; i=i+1) {
        print(a[i]);
    }
    return 0;
}