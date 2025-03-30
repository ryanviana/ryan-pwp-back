import { IsString, IsArray, IsOptional, IsNotEmpty } from 'class-validator';

class RelatedPostDto {
  @IsString()
  @IsNotEmpty()
  slug: string;

  @IsString()
  @IsNotEmpty()
  title: string;

  @IsString()
  @IsNotEmpty()
  coverImage: string;
}

export class CreateBlogPostDto {
  @IsString()
  @IsNotEmpty()
  slug: string;

  @IsString()
  @IsNotEmpty()
  title: string;

  @IsString()
  @IsNotEmpty()
  date: string;

  @IsString()
  @IsNotEmpty()
  excerpt: string;

  @IsString()
  @IsNotEmpty()
  coverImage: string;

  @IsString()
  @IsNotEmpty()
  readingTime: string;

  @IsArray()
  @IsString({ each: true })
  @IsOptional()
  tags: string[];

  @IsString()
  @IsNotEmpty()
  content: string;

  @IsArray()
  @IsOptional()
  relatedPosts: RelatedPostDto[];
}
