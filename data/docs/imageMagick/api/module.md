[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[AcquireModuleInfo](module.html#AcquireModuleInfo) • [DestroyModuleList](module.html#DestroyModuleList) • [GetModuleInfo](module.html#GetModuleInfo) • [GetModuleInfoList](module.html#GetModuleInfoList) • [GetModuleList](module.html#GetModuleList) • [GetMagickModulePath](module.html#GetMagickModulePath) • [IsModuleTreeInstantiated](module.html#IsModuleTreeInstantiated) • [InvokeDynamicImageFilter](module.html#InvokeDynamicImageFilter) • [ListModuleInfo](module.html#ListModuleInfo) • [OpenModule](module.html#OpenModule) • [OpenModules](module.html#OpenModules) • [RegisterModule](module.html#RegisterModule) • [TagToCoderModuleName](module.html#TagToCoderModuleName) • [TagToFilterModuleName](module.html#TagToFilterModuleName) • [TagToModuleName](module.html#TagToModuleName) • [UnregisterModule](module.html#UnregisterModule)

## [AcquireModuleInfo](http://www.imagemagick.org/api/MagickCore/module_8c.html)

AcquireModuleInfo() allocates the ModuleInfo structure.

The format of the AcquireModuleInfo method is:
    
    
    ModuleInfo *AcquireModuleInfo(const char *path,const char *tag)
    

A description of each parameter follows:

    
    

path
    the path associated with the tag. 
    
tag
    a character string that represents the image format we are looking for. 
    

## [DestroyModuleList](http://www.imagemagick.org/api/MagickCore/module_8c.html)

DestroyModuleList() unregisters any previously loaded modules and exits the module loaded environment.

The format of the DestroyModuleList module is:
    
    
    void DestroyModuleList(void)
    

## [GetModuleInfo](http://www.imagemagick.org/api/MagickCore/module_8c.html)

GetModuleInfo() returns a pointer to a ModuleInfo structure that matches the specified tag. If tag is NULL, the head of the module list is returned. If no modules are loaded, or the requested module is not found, NULL is returned.

The format of the GetModuleInfo module is:
    
    
    ModuleInfo *GetModuleInfo(const char *tag,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

tag
    a character string that represents the image format we are looking for. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetModuleInfoList](http://www.imagemagick.org/api/MagickCore/module_8c.html)

GetModuleInfoList() returns any modules that match the specified pattern.

The format of the GetModuleInfoList function is:
    
    
    const ModuleInfo **GetModuleInfoList(const char *pattern,
      size_t *number_modules,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
number_modules
     This integer returns the number of modules in the list. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetModuleList](http://www.imagemagick.org/api/MagickCore/module_8c.html)

GetModuleList() returns any image format modules that match the specified pattern.

The format of the GetModuleList function is:
    
    
    char **GetModuleList(const char *pattern,const MagickModuleType type,
      size_t *number_modules,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

pattern
    Specifies a pointer to a text string containing a pattern. 
    
type
    choose from MagickImageCoderModule or MagickImageFilterModule. 
    
number_modules
     This integer returns the number of modules in the list. 
    
exception
    return any errors or warnings in this structure. 
    

## [GetMagickModulePath](http://www.imagemagick.org/api/MagickCore/module_8c.html)

GetMagickModulePath() finds a module with the specified module type and filename.

The format of the GetMagickModulePath module is:
    
    
    MagickBooleanType GetMagickModulePath(const char *filename,
      MagickModuleType module_type,char *path,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

filename
    the module file name. 
    
module_type
    the module type: MagickImageCoderModule or MagickImageFilterModule. 
    
path
    the path associated with the filename. 
    
exception
    return any errors or warnings in this structure. 
    

## [IsModuleTreeInstantiated](http://www.imagemagick.org/api/MagickCore/module_8c.html)

IsModuleTreeInstantiated() determines if the module tree is instantiated. If not, it instantiates the tree and returns it.

The format of the IsModuleTreeInstantiated() method is:
    
    
    IsModuleTreeInstantiated()
    

## [InvokeDynamicImageFilter](http://www.imagemagick.org/api/MagickCore/module_8c.html)

InvokeDynamicImageFilter() invokes a dynamic image filter.

The format of the InvokeDynamicImageFilter module is:
    
    
    MagickBooleanType InvokeDynamicImageFilter(const char *tag,Image **image,
      const int argc,const char **argv,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

tag
    a character string that represents the name of the particular module. 
    
image
    the image. 
    
argc
    a pointer to an integer describing the number of elements in the argument vector. 
    
argv
    a pointer to a text array containing the command line arguments. 
    
exception
    return any errors or warnings in this structure. 
    

## [ListModuleInfo](http://www.imagemagick.org/api/MagickCore/module_8c.html)

ListModuleInfo() lists the module info to a file.

The format of the ListModuleInfo module is:
    
    
    MagickBooleanType ListModuleInfo(FILE *file,ExceptionInfo *exception)
    

A description of each parameter follows.

file

An pointer to a FILE.

exception

return any errors or warnings in this structure.

## [OpenModule](http://www.imagemagick.org/api/MagickCore/module_8c.html)

OpenModule() loads a module, and invokes its registration module. It returns MagickTrue on success, and MagickFalse if there is an error.

The format of the OpenModule module is:
    
    
    MagickBooleanType OpenModule(const char *module,ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

module
    a character string that indicates the module to load. 
    
exception
    return any errors or warnings in this structure. 
    

## [OpenModules](http://www.imagemagick.org/api/MagickCore/module_8c.html)

OpenModules() loads all available modules.

The format of the OpenModules module is:
    
    
    MagickBooleanType OpenModules(ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

exception
    return any errors or warnings in this structure. 
    

## [RegisterModule](http://www.imagemagick.org/api/MagickCore/module_8c.html)

RegisterModule() adds an entry to the module list. It returns a pointer to the registered entry on success.

The format of the RegisterModule module is:
    
    
    ModuleInfo *RegisterModule(const ModuleInfo *module_info,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

info
    a pointer to the registered entry is returned. 
    
module_info
    a pointer to the ModuleInfo structure to register. 
    
exception
    return any errors or warnings in this structure. 
    

## [TagToCoderModuleName](http://www.imagemagick.org/api/MagickCore/module_8c.html)

TagToCoderModuleName() munges a module tag and obtains the filename of the corresponding module.

The format of the TagToCoderModuleName module is:
    
    
    char *TagToCoderModuleName(const char *tag,char *name)
    

A description of each parameter follows:

    
    

tag
    a character string representing the module tag. 
    
name
    return the module name here. 
    

## [TagToFilterModuleName](http://www.imagemagick.org/api/MagickCore/module_8c.html)

TagToFilterModuleName() munges a module tag and returns the filename of the corresponding filter module.

The format of the TagToFilterModuleName module is:
    
    
    void TagToFilterModuleName(const char *tag,char name)
    

A description of each parameter follows:

    
    

tag
    a character string representing the module tag. 
    
name
    return the filter name here. 
    

## [TagToModuleName](http://www.imagemagick.org/api/MagickCore/module_8c.html)

TagToModuleName() munges the module tag name and returns an upper-case tag name as the input string, and a user-provided format.

The format of the TagToModuleName module is:
    
    
    TagToModuleName(const char *tag,const char *format,char *module)
    

A description of each parameter follows:

    
    

tag
    the module tag. 
    
format
    a sprintf-compatible format string containing s where the upper-case tag name is to be inserted. 
    
module
    pointer to a destination buffer for the formatted result. 
    

## [UnregisterModule](http://www.imagemagick.org/api/MagickCore/module_8c.html)

UnregisterModule() unloads a module, and invokes its de-registration module. Returns MagickTrue on success, and MagickFalse if there is an error.

The format of the UnregisterModule module is:
    
    
    MagickBooleanType UnregisterModule(const ModuleInfo *module_info,
      ExceptionInfo *exception)
    

A description of each parameter follows:

    
    

module_info
    the module info. 
    
exception
    return any errors or warnings in this structure. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](module.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
