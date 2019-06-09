#pragma once

#include "cfu_10.h"

class Cfu_5 : public Cfu_10
{
    private:
        int q;

    
    public:
        Cfu_5(int q=110);
		virtual int run_opp();
};
