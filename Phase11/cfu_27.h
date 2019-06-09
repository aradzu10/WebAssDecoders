#pragma once

#include "cfu_16.h"

class Cfu_27 : public Cfu_16
{
    private:
        int b;

    
    public:
        Cfu_27(int b=40);
		virtual int run_opp();
};
