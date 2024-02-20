# 이진 트리 구현해보기


def solution(n):
    answer = 0
    tree = [1*i for i in range(10)]
    # 트리 root 부터 출력하기
    heap_size = len(tree)
    print(tree)
    def tree_value(root, tree, heap_size ):
        heap_size = len(tree)
        
        
        left_index = root * 2
        right_index = root * 2 +1
        if right_index >= heap_size:
            #print(tree[right_index])
            return 1
        if left_index >= heap_size-1:
            #print(tree[left_index])
            return 1
        print(tree[root])
        print(tree[left_index])
        print(tree[right_index])
        root +=1
        return tree_value(root, tree,heap_size)
    
    tree_value(tree[1],tree,heap_size)
    
    
    return answer
