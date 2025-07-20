def quad_to_coord(d: int, quad_str: str):
    if d == 0:
        return (0, 0)
    
    half = 2**(d-1)
    
    x, y = quad_to_coord(d-1, quad_str[1:])
    
    q = quad_str[0]
    if q == '1':
        return (x+half, y+half)
    elif q == '2':
        return (x, y+half)
    elif q == '3':
        return (x, y)
    elif q == '4':
        return (x+half, y)
    
def coord_to_quad(d: int, x: int, y: int):
    if d == 0:
        return ''
    
    half = 2**(d-1)
    
    if x >= half and y >= half:
        return '1' + coord_to_quad(d-1, x-half, y-half)
    
    elif x < half and y >= half:
        return '2' + coord_to_quad(d-1, x, y-half)

    elif x < half and y < half:
        return '3' + coord_to_quad(d-1, x, y)
    else:
        return '4' + coord_to_quad(d-1, x-half, y)

def solve():
    d, quad_str = input().strip().split()
    d = int(d)
    
    x, y = map(int, input().strip().split())
    
    start_x, start_y = quad_to_coord(d=d, quad_str=quad_str)
    
    end_x, end_y = start_x + x, start_y + y
    
    if not (0 <= end_x < 2**d and 0 <= end_y < 2**d):
        print(-1)
        exit()
    
    else:
        end_quad = coord_to_quad(d, end_x, end_y)
        print(end_quad)
        exit()
        
solve()