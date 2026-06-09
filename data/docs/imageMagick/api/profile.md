[Home](../index.html) [Download](../binary-releases.html) [Tools](../command-line-tools.html) [Command-line](../command-line-processing.html) [Resources](../resources.html) [Develop](api.html) [Search](http://nextgen.imagemagick.org/script/search.php) [Community](https://www.imagemagick.org/discourse-server/)

[CloneImageProfiles](profile.html#CloneImageProfiles) • [DeleteImageProfile](profile.html#DeleteImageProfile) • [DestroyImageProfiles](profile.html#DestroyImageProfiles) • [GetImageProfile](profile.html#GetImageProfile) • [GetNextImageProfile](profile.html#GetNextImageProfile) • [ProfileImage](profile.html#ProfileImage) • [RemoveImageProfile](profile.html#RemoveImageProfile) • [ResetImageProfileIterator](profile.html#ResetImageProfileIterator) • [SetImageProfile](profile.html#SetImageProfile) • [SyncImageProfiles](profile.html#SyncImageProfiles)

## [CloneImageProfiles](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

CloneImageProfiles() clones one or more image profiles.

The format of the CloneImageProfiles method is:
    
    
    MagickBooleanType CloneImageProfiles(Image *image,
      const Image *clone_image)
    

A description of each parameter follows:

    
    

image
    the image. 
    
clone_image
    the clone image. 
    

## [DeleteImageProfile](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

DeleteImageProfile() deletes a profile from the image by its name.

The format of the DeleteImageProfile method is:
    
    
    MagickBooleanTyupe DeleteImageProfile(Image *image,const char *name)
    

A description of each parameter follows:

    
    

image
    the image. 
    
name
    the profile name. 
    

## [DestroyImageProfiles](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

DestroyImageProfiles() releases memory associated with an image profile map.

The format of the DestroyProfiles method is:
    
    
    void DestroyImageProfiles(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [GetImageProfile](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

GetImageProfile() gets a profile associated with an image by name.

The format of the GetImageProfile method is:
    
    
    const StringInfo *GetImageProfile(const Image *image,const char *name)
    

A description of each parameter follows:

    
    

image
    the image. 
    
name
    the profile name. 
    

## [GetNextImageProfile](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

GetNextImageProfile() gets the next profile name for an image.

The format of the GetNextImageProfile method is:
    
    
    char *GetNextImageProfile(const Image *image)
    

A description of each parameter follows:

    
    

hash_info
    the hash info. 
    

## [ProfileImage](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

ProfileImage() associates, applies, or removes an ICM, IPTC, or generic profile with / to / from an image. If the profile is NULL, it is removed from the image otherwise added or applied. Use a name of '*' and a profile of NULL to remove all profiles from the image.

ICC and ICM profiles are handled as follows: If the image does not have an associated color profile, the one you provide is associated with the image and the image pixels are not transformed. Otherwise, the colorspace transform defined by the existing and new profile are applied to the image pixels and the new profile is associated with the image.

The format of the ProfileImage method is:
    
    
    MagickBooleanType ProfileImage(Image *image,const char *name,
      const void *datum,const size_t length,const MagickBooleanType clone)
    

A description of each parameter follows:

    
    

image
    the image. 
    
name
    Name of profile to add or remove: ICC, IPTC, or generic profile. 
    
datum
    the profile data. 
    
length
    the length of the profile. 
    
clone
    should be MagickFalse. 
    

## [RemoveImageProfile](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

RemoveImageProfile() removes a named profile from the image and returns its value.

The format of the RemoveImageProfile method is:
    
    
    void *RemoveImageProfile(Image *image,const char *name)
    

A description of each parameter follows:

    
    

image
    the image. 
    
name
    the profile name. 
    

## [ResetImageProfileIterator](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

ResetImageProfileIterator() resets the image profile iterator. Use it in conjunction with GetNextImageProfile() to iterate over all the profiles associated with an image.

The format of the ResetImageProfileIterator method is:
    
    
    ResetImageProfileIterator(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

## [SetImageProfile](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

SetImageProfile() adds a named profile to the image. If a profile with the same name already exists, it is replaced. This method differs from the ProfileImage() method in that it does not apply CMS color profiles.

The format of the SetImageProfile method is:
    
    
    MagickBooleanType SetImageProfile(Image *image,const char *name,
      const StringInfo *profile)
    

A description of each parameter follows:

    
    

image
    the image. 
    
name
    the profile name, for example icc, exif, and 8bim (8bim is the Photoshop wrapper for iptc profiles). 
    
profile
    A StringInfo structure that contains the named profile. 
    

## [SyncImageProfiles](http://www.imagemagick.org/api/MagickCore/profile_8c.html)

SyncImageProfiles() synchronizes image properties with the image profiles. Currently we only support updating the EXIF resolution and orientation.

The format of the SyncImageProfiles method is:
    
    
    MagickBooleanType SyncImageProfiles(Image *image)
    

A description of each parameter follows:

    
    

image
    the image. 
    

[Donate](../support.html) • [Sitemap](../sitemap.html) • [Related](../links.html) • [Architecture](../architecture.html)

[Back to top](profile.html#) • [Public Key](http://pgp.mit.edu:11371/pks/lookup?op=get&search=0x89AB63D48277377A) • [Contact Us](http://nextgen.imagemagick.org/script/contact.php)

© 1999-2016 ImageMagick Studio LLC
