#pragma once

#include "cfu_23.h"

class Cfu_11 : public Cfu_23
{
    private:
        int i;

    
    public:
        Cfu_11(int i=32);
		virtual int run_opp();
};
