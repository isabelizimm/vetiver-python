import nest_asyncio
import warnings

def _jupyter_nb():

    notebook = True
    try:
        from IPython import get_ipython
    except ImportError:
        notebook = False

    if notebook:
        warnings.warn(
            "WARNING: Jupyter Notebooks are not considered stable environments for production code"
        )
        nest_asyncio.apply()
    else:
        pass
