#pragma once

#include "cfu_16.h"

class Cfu_20 : public Cfu_16
{
    private:
        int z;

    
    public:
        Cfu_20(int z=123);
		virtual int run_opp();
};
