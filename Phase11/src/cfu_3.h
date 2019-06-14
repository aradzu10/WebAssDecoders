#pragma once

#include "cfu_16.h"

class Cfu_3 : public Cfu_16
{
    private:
        int d;

    
    public:
        Cfu_3(int d=125);
		virtual int run_opp();
};
