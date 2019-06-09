#pragma once

#include "cfu_6.h"

class Cfu_24 : public Cfu_6
{
    private:
        int c;

    
    public:
        Cfu_24(int c=80);
		virtual int run_opp();
};
