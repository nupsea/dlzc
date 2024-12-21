# Serving Clothing model 

## Pre-req
Run and Follow steps in c10_k.ipynb

## Test locally

```bash
python gateway_v01.py
```
>   {'dress': -1.8798637390136719, 'hat': -4.756310939788818, 'longsleeve': -2.3595337867736816, 'outwear': -1.0892633199691772, 'pants': 9.903782844543457, 'shirt': -2.8261797428131104, 'shoes': -3.648311138153076, 'shorts': 3.2411556243896484, 'skirt': -2.612095594406128, 't-shirt': -4.852035999298096}

Wrap gateway.py to include within Flask application. 


```bash
python test.py
```
>  [model OUTPUT]: {'dress': -1.8798637390136719, 'hat': -4.756310939788818, 'longsleeve': -2.3595337867736816, 'outwear': -1.0892633199691772, 'pants': 9.903782844543457, 'shirt': -2.8261797428131104, 'shoes': -3.648311138153076, 'shorts': 3.2411556243896484, 'skirt': -2.612095594406128, 't-shirt': -4.852035999298096}


