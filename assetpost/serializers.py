from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import PostEntry

User = get_user_model()

class EntrySerializer(serializers.ModelSerializer):

    links = serializers.SerializerMethodField()
    
    class Meta:
        model = PostEntry
        fields = ('client', 'job_number', 'cell_number', 'post_title', 'date', 'post_type', 'post_round', 'links')

    def get_links(self, obj):
        request = self.context['request']
        return {'self': reverse('postentry-detail', kwargs={'pk': obj.pk},request=request),
    }


    def findMult(a, b, c):
        nums = []
        total = 0
        for i in range(a, c, a):
            if a%i == 0:
                nums.append(i)
        for e in range(0, c, b):
            if b%i == 0:
                nums.append(e)
        for num in nums:
            total += num
        return total

def evenfib():
    total = 0
    result = 0
    n = 2
    nums = []
    def fib(n):
        if n < 2:
            return 2
        return fib(n-2) + fib(n-1)
    while total < 4000000:
        if fib(n) % 2 == 0:
            nums.append(fib(n))
        total += fib(n)
        return fib(n+1)
    for num in nums:
        result += num
    return result

import operator

def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L)/2)
        right = mergeSort(L[middle:], compare)
        left = mergeSort(L[:middle], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if compare (left[i], right[j]):
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    while i < len(left):
        result.append(left[i])
    while i < len(right):
        result.append(right[i])
    return result

def selectSort(L):
    for i in range(len(L)-1):
        minIndx = i
        minVal = L[i]
        j = i + 1

        while j < len(L):
            if minVal < L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[i+1]
        L[i+1] = temp
    return L


class intSet(object):
    '''
    '''
    def __init__(self):
        self.vals = []
        
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + "not found")

    def intersect(self, other):
        self.iSet = []

        for i in self.vals:
            if i in other.vals:
                self.iSet.append(i)
        if len(self.iSet) == 0:
            return "there is no intersection between sets"
        return "{" + ",".join([str(e) for e in self.iSet]) + "}"

    def len(self):
        return len(self.vals)

    def __str__(self):
        self.vals.sort()
        return "{" + ",".join([str(e) for e in self.vals]) + "}" 

class Queue(object):
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        try:
            return self.items.pop()
        except:
            raise ValueError()

    def __str__(self):
        return self.items

import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getLastName(self):
        return self.lastName

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return ((datetime.date.today()-self.birthday).days)/365

    def __lt__(self, other):
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        return self.name

class MITPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.IdNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.IdNum

    def __lt__(self, other):
        return self.IdNum < other.IdNum


class UG(MITPerson):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear

    def getClass(self):
        return self.year

class Grad(MITPerson):
    pass

def isStudent(obj):
    return isinstance(obj,UG) or isinstance(obj,Grad)

