#pragma once

#include "cfu_13.h"

class Cfu_1 : public Cfu_13
{
    private:
        int d;

    
    public:
        Cfu_1(int d=115);
		virtual int run_opp();
};
