#include <stdio.h>

// Loop function for checking
double loop(double x, int n) {
    double sum = x - 1;
    double p = x - 1;

    for(int i = 1; i < n; i++) {
        p = -p * i * (x-1) / (i+1);
        sum += p;
        printf("p = %lf\t", p);
        printf("sum = %lf\n", sum);
    }
    return sum;
}


//Recursive function on returning
double returningInner(double x, int n, double *sum){
    double p;

    if(n == 1){
        p = x - 1;
        printf("p = %lf, n = %d, sum = %lf\n", p, n, *sum);
    }else {
        p = -returningInner(x, n - 1, sum) * (n - 1) * (x - 1) / n;
        *sum += p;
        printf("p = %lf, n = %d, sum = %lf\n", p, n, *sum);
    }
    return p;
}
//Recursive wrapper function on returning
double returning(double x, int n) {
    double sum = x - 1;
    returningInner(x,n,&sum);
    return sum;
}


//Recursive inner function on descent
double descentInner(double x, int n, double p, int i, double sum) {
    if(n != 1) {
        p = -p * i * (x - 1) / (i + 1);
        sum += p;
        printf("p = %lf, n = %d, sum = %lf\n", p, n, sum);
        sum = descentInner(x, n - 1, p, i + 1, sum);
        printf("p = %lf, n = %d, sum = %lf\n", p, n, sum);
    }
    return sum;
}
//Recursive wrapper function on descent
double descent(double x, int n) {
    double sum = x - 1;
    double p = x - 1;
    int i = 1;
    return descentInner(x, n, p, i, sum);
}


//Recursive inner combined function
double combinationInner(double x, int n, double p, int i, double sum) {
    if (n != 1) {
        p = -p * i * (x - 1) / (i + 1);
        printf("p = %lf, n = %d, sum = %lf\n", p, n, sum);
        sum = combinationInner(x, n - 1, p, i + 1, sum);
        sum += p;
        printf("p = %lf, n = %d, sum = %lf\n", p, n, sum);
    }
    return sum;
}
//Recursive wrapper combined function
double combination(double x, int n) {
    double sum = x - 1;
    double p = x - 1;
    int i = 1;
    return combinationInner(x, n, p, i, sum);
}


int main() {

    const double X = 1.5;
    const int N = 5;

    printf("\nResult of loop function is: %lf\n\n", loop(X, N));

    printf("\nResult of returning function is: %lf\n\n", returning(X, N));
    printf("\nResult of descent function is: %lf\n\n", descent(X, N));
    printf("\nResult of combined function is: %lf\n\n", combination(X, N));

    return 0;
}
