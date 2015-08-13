#include <iostream>
#include <algorithm>

using namespace std;

void  Memcpy(void *dst, void *src, size_t n) {
    char *ddst = (char *) dst;
    char *ssrc = (char *) src;
    while (ssrc) {
	*ddst++ = *ssrc++;
    }
}

void Memcpy2(void *dst, void *src, size_t n) {
    size_t remain = n % 4;
}

// stackoverflow
void memcpy_2(void* dest, void* src, int size)
{
    uint8_t *pdest = (uint8_t*) dest;
    uint8_t *psrc = (uint8_t*) src;

    int loops = (size / sizeof(uint32_t));
    for(int index = 0; index < loops; ++index)
    {
        *((uint32_t*)pdest) = *((uint32_t*)psrc);
        pdest += sizeof(uint32_t);
        psrc += sizeof(uint32_t);
    }

    loops = (size % sizeof(uint32_t));
    for (int index = 0; index < loops; ++index)
    {
        *pdest = *psrc;
        ++pdest;
        ++psrc;
    }
}

int main(int argc, char *argv[])
{
    char a [] = {'a','c','d'};
    char b [3];
    char *pa = a, *pb = b;
    Memcpy(pb, pa, 3);
    for (int i = 0; i < 3; i++)
	cout<<b[i]<<endl;
    return 0;
}
