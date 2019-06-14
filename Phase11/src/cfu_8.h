#pragma once

#include "cfu_21.h"

class Cfu_8 : public Cfu_21
{
    private:
        int r;

    
    public:
        Cfu_8(int r=44);
		virtual int run_opp();
};
