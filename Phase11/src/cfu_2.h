#pragma once

#include "cfu_7.h"

class Cfu_2 : public Cfu_7
{
    private:
        int b;

    
    public:
        Cfu_2(int b=101);
		virtual int run_opp();
};
