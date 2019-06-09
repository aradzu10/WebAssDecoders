#pragma once

#include "cfu_7.h"

class Cfu_16 : public Cfu_7
{
    private:
        int d;

    
    public:
        Cfu_16(int d=39);
		virtual int run_opp();
};
