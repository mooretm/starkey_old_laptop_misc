""" Combine (in)coherent dB values """

# Import data science packages
import numpy as np

def spl2upa(spl_val):
    SPL = 20 * 10**(spl_val/20)
    return SPL


def upa2spl(upa_val):
    upa = 20 * np.log10(upa_val/20)
    return upa


def il2upa(il_val):
    upa = 10**(il_val/10) * 10**-12
    return upa


def upa2il(upa_val):
    IL = 10 * np.log10(upa_val/10**-12)
    return IL


def add_coherent(db_spl):
    """ Use SPL to combine coherent signals """
    # db_spl: a list of levels
    upa = [spl2upa(db) for db in db_spl]
    total = sum(upa)
    SPL = upa2spl(total)
    return SPL


def add_incoherent(db_il):
    """ Use IL to combine incoherent signals """
    # db_il: a list of levels
    upa = [il2upa(db) for db in db_il]
    total = sum(upa)
    IL = upa2il(total)
    return IL


def get_db_incoherent(num_sources, desired_level):
    """ Find dB value for each single source to 
        achieve desired overall level
    """
    oal = add_incoherent(np.repeat(desired_level, num_sources))

    offset = 0.0
    while (oal > desired_level):
        offset += 0.01
        oal = add_incoherent(np.repeat(desired_level-offset, num_sources))
        #print(oal)
    
    print(f"Set each source to: {np.round(desired_level-offset, 1)} dB")
