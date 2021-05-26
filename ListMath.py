class ListMath:
    def __init__(self):
        pass

    def maximum(self, ls):
        """
        Return the maximum value in the list

        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        maximum : number
          Maximum value in the list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.max(ls)
        8
     
        """
        # check the length of the list 
        # if more than 0, then search for max
        if(len(ls) > 0):
            maximum= ls[0]  # assum the first element is the max
            
            # iterate through the list elements and compare it with current max
            for i in range(1, len(ls)):
                # if there is number greater than current max, 
                # then assign it to 'maximum'
                if (ls[i] > maximum):
                    maximum= ls[i]
                    
            return maximum
        # if the lsit is empty return "The list is empty."
        else:
            return "The list is empty."
            
    def minimum(self, ls):
        """
        Return the minimum value in the list
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        minimum: number
          Minimum value in the list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.minimum(ls)
        -6
     
        """
        # check the length of the list 
        # if more than 0, then search for min
        if(len(ls) > 0):
            minimum= ls[0]   # assum the first element is the min
            
            # iterate through the list elements and compare it with current min
            for i in range(1, len(ls)):
                # if there is number less than current min, 
                # then assign it to 'minimum'
                if (ls[i] < minimum):
                    minimum= ls[i]
                    
            return minimum
        # if the lsit is empty return "The list is empty."
        else:
            return "The list is empty."

    def max_squared(self, ls):
        """
        Return the maximum value squared
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        max_squar : number
          Maximum value squared in the list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.max_squared(ls)
        64
     
        """           
        max_ = self.max(ls)  # maximumnumber in the list 'ls'
        max_squar = max_**2  # calculate the square for max
        return max_squar 
  
    def length(self, ls):
        """
        Return the length of the list
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        list_len : int
           Length of the list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.length(ls)
        6
     
        """
        list_len = len(ls)
        return list_len
    
    def positive_sum(self, ls):
        """
        Return the sum of all positive numbers in the list
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        sum_pos : number
           Sum of all positive numbers in the list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.positive_sum(ls)
        15
     
        """   
        list_pos = [i for i in ls if i > 0]  # filter positive number 
        sum_pos = sum(list_pos)  # count negative number in the list
        return sum_pos

    def negative_count(self, ls):  
        """
        Return the count of all negative number in the list
        
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        count_neg : int
           Count of the negative in list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.negative_count(ls)
        -6
    
         
        """        
        list_neg = [1 for i in ls if i < 0]  # create new list to store 1 if there is negative number 
        count_neg = sum(list_neg)  # count negative number in the list
        return count_neg
    
    def reverse_list(self, ls):
        """
        Return the reverse of list
        
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        new_list : a list
           Reverse of list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.reverse_list(ls)
        [8, -6, 7, 5, -3, 4]
    
         
        """         
        new_list = []  # create new list
        # iterate through the list elements from list length to 0 (reversed)
        for i in reversed(range(len(ls))):
            new_list.append(ls[i])  # add element in new_list

        return new_list 
    
    def sum_total(self, ls):
        """
        Return the sum of all element in list
        
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        total : number
           Sum of all element in list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.sum_total(ls)
        15
    

        """         
        total = 0
        # iterate through the list elements
        for i in range(len(ls)):
            total += ls[i]  # add element to the total, total = total + ls[i]

        return total
    
    def average(self, ls):
        """
        Return the average of all element in list
        
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        average : number
           Average of all element in list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.average(ls)
        2.5
    
         
        """         
        total = self.sum_total(ls)  # call sum_total method
        average = total/len(ls)  # calculate the average
        return average
    
    def summary(self, ls):
        """
        Return summary about list
        
        
        Parameters
        ----------
        ls: a list 
            Input list.
            
        Returns
        -------
        out : dict
           Summary about list `ls`.
        
        Examples
        --------
        >>> ls = [4, -3, 5, 7, -6, 8]
        >>> List.summary(ls)
        {'Sum Total': 15, 'Average': 2.5, 'Minimum': -6, 'Maximum': 8, 'Length': 6}
    
         
        """
            
        out = dict()
        out['Sum Total'] = self.sum_total(ls)
        out['Average'] = self.average(ls)
        out['Minimum'] = self.minimum(ls)
        out['Maximum'] = self.maximum(ls)
        out['Length'] = self.length(ls)
        return out
