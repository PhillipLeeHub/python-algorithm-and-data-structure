# // Find the max sum path from the root to a leaf of a binary tree
# // example
# //           5
# //     2          3
# //  8    10          1


# class node():
#   self.val
#   self.right
#   self.left

# //  return 17

# //  17 = 5 + 2 + 10

'''
DFS 
  recursive
  iterative
'''
max_result = float('-inf')
def get_max_path(root):
  recursive(root)
  return max_result

def recursive(root, running_sum=0):
  if not root:
    return 
    
  running_sum += root.val
  
  recursive(root.left, running_sum)
  recursive(root.right, running_sum)
    
  if !root.left and !root.right:
    max_result = max(running_sum, max_result)
    
    


# //           -6
# //     20           5
# // 2      -10   -20    30
# // 			                  -7
''' Generate all paths O(n) where n number nodes
[-6, 20, 2]
[-6, 20, -10]
[-6, 5, 30, -7]

# O(n)
Use sliding window to calculate max continuous subarray
    <  35   >    max = 35
    
    
# Time O(n)
# Space O(n)
'''
# // return 35
# // 35 = 5 + 30
max_result = float('-inf')
g_list = []
def get_max_path(root):
  recursive(root, [])

def recursive(root, curr_list):
  if not root:
    return 
    
  curr_list.append(root.val)
  
  recursive(root.left, curr_list[:])
  recursive(root.right, curr_list[:])
    
  if !root.left and !root.right:
    g_list.append(curr_list)


'''
[[-6, 20, 2]
[-6, 20, -10]
[-6, 5, 30, -7]]
'''
def slideing_win(path_list):
  for curr_list in path_list:
    max_value = float('-int')
    prev_value = 0
    for i, value in enumerate(curr_list):
      max_value = max(value, value+prev_value)
      



----------------
//               1 (0,0)
//       2 (-1,1)                 3 (1,1)
//  4 (-2,2)              6 (0,2)        7(2,2)


// x=-2 [4]
// x=-1 [2]
// x=0   [1,6]
// x=1   [3]
// x=2   [7]


// [
//    [4],
//    [2],
//    [1,6],
//    [3],
//    [7]
//]

// 1. in each group, nodes should be ordered by y coordinate
// 2. order the group by x coordinates


TreeNode {
  left:
  right:
  val: 
}

// [[TreeNode]] groupByX (TreeNode root)
import Queue
def tree_to_dict(root):
  '''
  dict = {
  -2: ([4], 2),
  -1: [1]
  0: [([1],0),([6],2)]
  } (list, y )
  
  DFS
  '''
  stack = [(root, 0, 0)]
  x_y_dict = {}
  min_left = 0
  max_right = 0
  while(stack):
    node, x, y = stack.pop()
    min_left = min(min_left, x);
    max_right = max(max_right, x);
    
    if level in x_y_dict:
      x_y_dict[x] = x_y_dict[x].append([node.val, y])
    else:
      x_y_dict[x] = [[node.val, y]
    
    if node.left:
      stack.append((node.left, x-1, y+1))
    
    if node.right:
      stack.append((node.right, x+1, y+1))
    
  unsorted_list = []
  # Loop through dict
  for x in range(min_left, max_right+1):                   
    unsorted_list.append(x_y_dict[x])
    

  # now sort by x
  sorted_list = unsorted_list.sorted(lambda x: x[0])

  return sorted_list












---------------
# // Please design the api for an online library reservation system.  Use object oriented principles,
# // and don't worry about the database implementation behind the objects.

# // Please implement at least the following three methods, and take into account
# // how the state of the system should be evaluated, and will change in each case.

# // checkOut
# // searchForBook
# // assessFinesForUser

# // Requirements to take into account:
# // A user may search for books by name, author, category (mystery, etc.)
# // The library has a catalog of book titles, and there may be 0-N copies of the book in stock
# // A book may be checked out for up to 3 weeks
# // A user may have up to 3 books checked out at any given time
# // A user may renew a book up to 2 times
# // Overdue books will be fined at the rate of $.50/day

'''
lib_rules = {
  book_limit = 3, 
  book_duration = 3 weeks,  
}

user = {
  user_books= [
  book_id : {
    date_of_checkout = date,
    renew_count = int,
    book: ref
    }
  ],
  account_id: uuid()
  balance_amount = int
}

book = {
  name: string
  author: string
  category:string
  stock: int
}

'''

# // checkOut
# // searchForBook
# // assessFinesForUser

def checkOut(books, user):
  # Check if books are availible 
  for book in books:
    match_book = book.find(book.name)
    if match_book.stock < 1:
      throw error
    
  
  # Check if user can checkout books
  if not validateUser(user):
    throw error
  
  
  # Process book checkout
 def validateUser(book, user_name):
  rule = collection.rule.find()
  user = collection.user.find(name)
  
  if len(user.user_books <= rule.book_limit):
    throw('Maximum books checked out.')
  
  
  for book in user.books:
    if user.user_books[book]:
      if user.user_books[book].renew_count >rule.book_limit:
        throw error
        
      if (user.user_books[book].date_of_checkout - book_duration) :
        throw error
  
  collection.book.update(name.stock, dec)
  
  checkout_book {
    date(),
    renew_count,
    book_ref
  }
  coolection.user.update(user, checkout_book)
     

def searchForbook(key_list, search_list):
  query_string = ''
  for index in key_list:
    query_string.append(key_list[index]: search_list[index])
  
  match_book_list = collection.book.find(query_string)

  return match_book_list

'''
 Search with data structure, Use dict with key as search string
 
 
'''












